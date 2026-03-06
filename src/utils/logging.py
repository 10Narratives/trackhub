import structlog
import logging
from typing import Any

def setup_logger(trace_level: str, trace_format: str) -> Any:
  logging.basicConfig(level=trace_level, format="%(message)s")

  processors = [
    structlog.stdlib.add_log_level,
    structlog.processors.TimeStamper(fmt="iso"),      
  ]

  if trace_format == "json":
    processors.append(structlog.processors.JSONRenderer())
  else:
    processors.append(structlog.dev.ConsoleRenderer())

  structlog.configure(
    processors=processors,
    wrapper_class=structlog.stdlib.BoundLogger,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
  )

  return structlog.get_logger()