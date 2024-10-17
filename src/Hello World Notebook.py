# Databricks notebook source
dbutils.widgets.dropdown("Who Am I", "Will Wang", ["Will Wang", "Jeremy Wang", "Hue", "Teddy", "Sethy", "Alex"])

# COMMAND ----------

name = dbutils.widgets.get("Who Am I")
print(f"My name is {name}")
