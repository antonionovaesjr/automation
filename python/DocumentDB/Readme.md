# Como usar essa função lambda ?

* É preciso criar uma função lambda com o código do arquivo ```start_stop_docDB.py```
* É preciso ter uma role coma  permissão default do lambda e também permissão de describe, start e stop RDS como indicado no arquivo  ```policy-iam.json```
* Não é preciso instalar dependências
* Criar um scheduler no [EventBridge](https://console.aws.amazon.com/scheduler/home?region=us-east-1#schedules) com o destino a uma AWS Lambda Invoke
* A entrada dos dados a ser enviada para o Lambda pelo EventBridge Scheduler será:

```json
 {
   "DOCDB_NAME":["my-codumentdb-A","my-codumentdb-B","my-codumentdb-C"],
   "DOCDB_ACTION":"start"
  }
```
