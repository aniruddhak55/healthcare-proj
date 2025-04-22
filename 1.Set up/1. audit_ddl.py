# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table  tt_hc_adb_ws.audit.load_logs 

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.gold;

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into audit.load_logs(data_source, tablename, numberofrowscopied, watermarkcolumnname, loaddate) values ('hos-a','dbo.departments','20','','2025-04-13T06:34:07.8490890Z')
