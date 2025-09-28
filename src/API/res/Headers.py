import os
try:
	from cerebras.cloud.sdk import Cerebras
	ai_client = Cerebras(api_key="csk-vkv299rfjj4t2dk89h599p4nwjnej8xt9pd4fwcpw4d84tr3")
except Exception:
	# Fallback stub for environments without 'cerebras' installed.
	class _StubClient:
		def __init__(self, *a, **k):
			pass
		def predict(self, *a, **k):
			return {"error": "cerebras not installed"}
	ai_client = _StubClient()