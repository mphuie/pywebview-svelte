<script>

let ret = '';
function callTest() {
  console.log('click!');
  pywebview.api.hello({ test:'world'}).then(function(response) {
    ret = response
  })

}
</script>

<h1>pywebview-svelte</h1>

<button on:click={callTest}>Call python test function</button>

{#each ret as r}
<li>{r}</li>
{/each}

