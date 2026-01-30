import logging

from karafun_manager.repositories.notificacion_repository import NotificationRepository

logger = logging.getLogger(__name__)

class NotificationService:

    @staticmethod
    def notificar_error(detalles_error: dict):
        try:
            return NotificationRepository.crear_notificacion(
                tipo_notificacion_id=6,     # tipo_notificacion_id (6 = Error Microservicio Ms_Karafun) 
                detalles=detalles_error,    # Detalles notificación
                cliente_id=None,            # cliente_id
                usuario_id=None,            # usuario_id
                rol_id=1                    # rol_id (1 = Administrador)
            )
        except Exception:
            logger.exception(
                "Error al registrar la notificación"
            )
            return None
