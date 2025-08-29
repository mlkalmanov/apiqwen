from openai import OpenAI
import datetime

system_prompt = '''
Ты технический переводчик. на вход ты будешь получать текст из документации кода.
Тебе необходимо будет перевести саму документацию на русский, вывести её переведенный вариант и
написать объяснение смысла этой документации простым для далёкого профессиональной деятельности языком
'''
user_prompt = '''
Client manager that uses aio_pika for inter-process messaging under asyncio.
                                    This class implements a client manager backend for event sharing across multiple processes, using RabbitMQ
                                    To use a aio_pika backend, initialize the :class:`Server` instance as follows::
                                        url = 'amqp://user:password@hostname:port//'
                                        server = socketio.Server(client_manager=socketio.AsyncAioPikaManager(url))
                                    :param url: The connection URL for the backend messaging queue. Example
                                                connection URLs are ``'amqp://guest:guest@localhost:5672//'``
                                                for RabbitMQ."
                                    :param channel: The channel name on which the server sends and receives
                                                    notifications. Must be the same in all the servers.
                                                    With this manager, the channel name is the exchange name
                                                    in rabbitmq"
                                    :param write_only: If set to ``True``, only initialize to emit events. The
                                     default of ``False`` initializes the class for emitting
                                    and receiving.
'''

client = OpenAI(api_key="", base_url="")

response = client.chat.completions.create(
    model="qwen/qwen3-14b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    stream=False
)
current_time = datetime.datetime.now()
ans = response.choices[0].message.content

with open('ans.txt', 'a', encoding='utf-8') as file:
    file.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
    file.write(user_prompt + '\n')
    file.write(ans + '\n' + '\n')
