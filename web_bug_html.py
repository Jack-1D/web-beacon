def web_bug():
    return '''
<h1>I know you've read this mail</h1>
<div style="color:red">By webhook</div>
<img height="1" width="1" style="display:none" src="{webhook}">
'''