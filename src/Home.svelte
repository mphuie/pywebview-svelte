<script>
  import { onMount } from "svelte";
  import { config } from "./configFile.js";

  let config_value;
  let ret = "";

  let unsub = config.subscribe(value => {
    config_value = value;
  });


  function callTest() {
    console.log("click!");
    pywebview.api.hello({ test: "world" }).then(function(response) {
      ret = response;
    });
  }
</script>

<h1>pywebview-svelte</h1>

<button on:click={callTest}>Call python test function</button>

{#each ret as r}
  <li>{r}</li>
{/each}

<h1>Config</h1>
<pre>{JSON.stringify(config_value)}</pre>
