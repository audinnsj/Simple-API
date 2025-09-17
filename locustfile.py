from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(3.0,10.5)

    @task
    def get_file_10kb(self):
        self.client.get("/file/10kb")

    @task
    def get_file_100kb(self):
        self.client.get("/file/100kb")

    @task
    def get_file_1mb(self):
        self.client.get("/file/1mb")

    @task
    def get_file_5mb(self):
        self.client.get("/file/5mb")

    @task
    def get_file_10mb(self):
        self.client.get("/file/10mb")