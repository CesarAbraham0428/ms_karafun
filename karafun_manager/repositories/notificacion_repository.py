import json
from django.db import connection

class NotificationRepository:

    @staticmethod
    def crear_notificacion(
        tipo_notificacion_id: int,
        detalles: dict,
        cliente_id: int | None,
        usuario_id: int | None,
        rol_id: int
    ) -> dict | None:

        detalles_json = json.dumps(
            {"datos": detalles},
            ensure_ascii=False
        )

        sql = """
            SELECT
                retorno[1] AS codigo,
                retorno[2] AS mensaje,
                retorno[3] AS datos
            FROM spi_notificacion(%s, %s, %s, %s, %s) AS retorno
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                [
                    tipo_notificacion_id,
                    detalles_json,
                    cliente_id,
                    usuario_id,
                    rol_id
                ]
            )

            row = cursor.fetchone()

        if not row:
            return None

        return {
            "codigo": row[0],
            "mensaje": row[1],
            "datos": row[2],
        }
