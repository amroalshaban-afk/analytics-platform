from slack_bolt.context.assistant.async_assistant_utilities import AsyncAssistantThreadContextStore
from slack_bolt.context.assistant.thread_context import AssistantThreadContext
from typing import Dict, Optional
import json

from utils.db import DB
from initialize_dbs import operations


class AsyncPostgresAssistantContextStore(AsyncAssistantThreadContextStore):
    
    def __init__(
        self,
        db: DB = operations
    ):
        self._db = db
    
    async def save(self, *, channel_id: str, thread_ts: str, context: Dict[str, str]) -> None:

        await self._db.execute(
            """
                INSERT INTO SLACK_ASSISTANT_CONTEXT_STORE (
                    CHANNEL_ID, THREAD_TS, USER_ID,
                    TEAM_ID, CONTEXT, PAYLOAD
                )
                VALUES (%s::text, %s::text, %s::text, %s::text, %s::jsonb, %s::jsonb)

                ON CONFLICT (CHANNEL_ID, THREAD_TS)
                DO UPDATE SET
                    CONTEXT = EXCLUDED.CONTEXT,
                    PAYLOAD = EXCLUDED.PAYLOAD
            """,
            (channel_id, thread_ts, context['user_id'], context['team_id'], json.dumps(context['context']), json.dumps(context['payload'])),
            fetch=False
        )


    async def find(self, *, channel_id: str, thread_ts: str) -> Optional[AssistantThreadContext]:

        data = await self._db.execute(
            """
                SELECT PAYLOAD
                FROM SLACK_ASSISTANT_CONTEXT_STORE
                WHERE CHANNEL_ID = %s::text
                AND THREAD_TS = %s::text
            """,
            (channel_id, thread_ts),
            fetch=True
        )

        if data:
            return AssistantThreadContext(json.loads(data[0]))
        
        return None
