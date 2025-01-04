//usr/bin/go run $0 $@ ; exit
package main

import (
	"os"
	"flag"
  "log"
  "html/template"
)


const (

	elementDoc = `
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Elements in HTML</title>
  
    <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
  </head>
  <body>

    <elements-api
      id="docs"
      router="hash"
    />
    <script type="application/json" id="oas-data">
{{ .API }}    </script>
    <script>
  (() => {
    const data = document.getElementById('oas-data');
    const docs = document.getElementById('docs');
    docs.apiDescriptionDocument = data.innerHTML;
  })();
    </script>
  </body>
</html>	
`
)


func main() {

	flag.Parse()

    jsonData, err := os.ReadFile(flag.Arg(0))
    if err != nil {
        log.Fatalf("can't read file %v", err)
    }

    tmp := template.Must(template.New("html").Parse(elementDoc))

    tmp.Execute(os.Stdout, map[string]any{
        "API": template.JS(jsonData),
    })
}



