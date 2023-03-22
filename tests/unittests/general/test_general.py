import json
import tempfile

from autogluon.cloud.backend import SagemakerBackend


def test_generate_trust_relationship_and_iam_policy():
    with tempfile.TemporaryDirectory() as root:
        backend = SagemakerBackend(local_output_path="dummy", cloud_output_path="dummy", predictor_type="dummy")
        paths = backend.generate_default_permission(account_id="foo", cloud_output_bucket="foo", output_path=root)
        trust_relationship_path, iam_policy_path = paths["trust_relationship"], paths["iam_policy"]
        for path in [trust_relationship_path, iam_policy_path]:
            with open(path, "r") as file:
                document = json.load(file)
                statement = document.get("Statement", None)
                assert statement is not None
                assert len(statement) > 0
