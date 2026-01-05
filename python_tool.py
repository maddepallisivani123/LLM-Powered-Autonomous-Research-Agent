def run_python(code_request):
    try:
        local_vars = {}
        exec(code_request, {}, local_vars)
        return str(local_vars)
    except Exception as e:
        return f"Python execution error: {e}"
