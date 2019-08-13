<script>
  import { config } from "./configFile.js";

  let config_value = {};
  let unsub = config.subscribe(value => {
    config_value = JSON.stringify(value);
  });

  let saveConfig = () => {
      console.log("save!")
      pywebview.api.save_config(config_value).then(() =>
      {
          config.update(() => JSON.parse(config_value));
      })
  }
    
</script>
<style>
textarea { font-family: monospace; }
</style>

<textarea bind:value={config_value} cols="40" rows="10" />
<br />
<button on:click={saveConfig}>Save Config</button>
