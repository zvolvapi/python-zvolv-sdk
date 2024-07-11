import uuid
import time
from logging import Handler

class KafkaHandler(Handler):
    """
    A handler class which writes formatted logging records to kafka topic.
    """

    def __init__(self, producer, topic, domain):
        Handler.__init__(self)
        self.topic = topic
        self.domain = domain
        self.producer = producer
        self.automation_uuid = None
        self.execution_id = None
        self.execution_by = 1234
        
    def close(self):
        if self.producer is None:
            return
        self.producer.close()
        super().close()

    def emit(self, record):
        if self.producer is None:
            return
        
        try:
             # Format the log message
            level = record.levelname
            status = 'success'
            if level != 'INFO':
                status = 'failure'
            log_body = {
                "domain": self.domain,
                "log_id": str(uuid.uuid4().hex),
                "execution_id": self.execution_id,
                "automation_uuid": self.automation_uuid,
                "executed_at": record.created,
                "executed_by": self.execution_by,
                "status": status,
                "message": record.getMessage(),
                "stack_trace": record.exc_text,
                "log_type": "inline"
            }
            self.producer.send(self.topic, value=log_body)
            self.producer.flush()
            return
        except Exception:
            self.handleError(record)

    def emitStatusLog(self, status, message, exc_text):
        if self.producer is None:
            return
        
        try:
            log_body = {
                "domain": self.domain,
                "log_id": str(uuid.uuid4().hex),
                "execution_id": self.execution_id,
                "automation_uuid": self.automation_uuid,
                "executed_at": time.time(),
                "executed_by": self.execution_by,
                "status": status,
                "message": message,
                "stack_trace": exc_text,
                "log_type": "status"
            }
            self.producer.send(self.topic, value=log_body)
            self.producer.flush()
            return
        except Exception as e:
            self.handleError(e)