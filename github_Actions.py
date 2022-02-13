from pprint import pprint
import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

load_dotenv()


class TriggerActions:

    def __init__(self):
        self.username = os.getenv("GITHUB_USER")
        self.password = os.getenv("GITHUB_TOKEN")
        self.HOST = os.getenv("HOST")
        self.REPO = os.getenv("REPO")

    def get_workflow_id(self):
        workflow_data = requests.get(f"{self.HOST}/repos/{self.username}/{self.REPO}/actions/workflows").json()
        for workflow in workflow_data["workflows"]:
            if "my-app" in workflow["name"]:
                pprint(workflow)
                return workflow["url"]

    def run_workflow(self, url, json_data={}):
        headers = {'content-type': 'application/vnd.github.v3+json'}
        res = requests.post(url, headers=headers, auth=HTTPBasicAuth(self.username, self.password), json=json_data)
        return res, res.json()

    def dispatch_workflow(self):
        URL = self.get_workflow_id()
        url = f"{URL}/dispatches"
        json_data = {
            "ref": "master",
        }
        response_code, data = self.run_workflow(url)
        return response_code

    def rerun_workflow(self):
        URL = f"{self.HOST}/repos/{self.username}/{self.REPO}/actions/runs"
        res = requests.get(URL)
        for workflow in res.json()["workflow_runs"]:
            if workflow["event"] == "workflow_dispatch":
                rerun_url = workflow["rerun_url"]
                response_code, data = self.run_workflow(rerun_url)
                return response_code, data


if __name__ == "__main__":
    ta = TriggerActions()
    print("Dispatching Workflow !!")
    dispatch_status_code, _ = ta.rerun_workflow()
    print(dispatch_status_code, "\n", _)
