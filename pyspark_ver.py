from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, sum, col
from pyspark.sql.types import IntegerType
import time
# Создаем экземпляр SparkSession
spark = SparkSession.builder \
.appName("BinaryFileReader") \
.getOrCreate()

# # Чтение бинарного файла
binary_file_path = "endian.bin"

def factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return len(Ans)

start=time.time()
factorUDF = udf(lambda z: factor(z), IntegerType())
binary_file_rdd = spark.sparkContext.binaryFiles(binary_file_path)

# Функция для чтения чисел по 4 байта
def read_int(data):
    return int.from_bytes(data[:4], 'big')

# Преобразование RDD в DataFrame
binary_file_df = binary_file_rdd.flatMap(lambda x: [(int(i/5), read_int(x[1][i:i+5])) for i in range(0, len(x[1]), 5)]) \
.toDF(["index", "number"])
binary_file_df= binary_file_df.withColumn('factor', factorUDF(col("number")))
bin_agg=binary_file_df.agg(sum("factor"))
# Отображение содержимого DataFrame
endd=time.time()-start

bin_agg.show()
print(endd)