<script>
  import Router from "svelte-spa-router";
  import {link} from 'svelte-spa-router'

  import Home from "./Home.svelte";
  import Config from "./Config.svelte";

  import { config } from "./configFile.js";

  // pywebview is deferred, wait until it's defined before loading config

  (async () => {
    while (
      !window.hasOwnProperty("pywebview") // define the condition as you like
    )
      await new Promise(resolve => setTimeout(resolve, 500));

    pywebview.api.get_config("test").then(function(response) {
      config.update(() => response);
    });
  })();

  const routes = {
    "/": Home,
    "/config": Config,
    "*": Home
  };
</script>

<a href="/" use:link>Home</a>
<a href="/config" use:link>Config</a>
<hr>

<Router {routes} />
