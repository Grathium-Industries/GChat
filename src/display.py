def displayVR(toRender):
	default = """
	<div class="split left">
	<iframe src=""" + toRender + """ class="viewframe" frameborder="0"></iframe>
	</div>

	<div class="split right">
	<iframe src=""" + toRender + """ class="viewframe" frameborder="0"></iframe>
	</div>
	"""

	return default
