+++
title= "Protractor en legacy code"
date= "2014-10-30"

+++

# Haciendo tests e2e en apps que ya tenemos hechas

## Introduccion
Digamos que entras en un proyecto donde existe una aplicacion con varios años en produccion, que usa como unicas librerias require y jQuery, todo lo demas esta hecho a mano, ademas como puedes suponer, no tiene ni un solo test.

Nos proponemos hacer tests sobre el codigo existente y asi implantarlos para futuras features.

## WebdriverJs (Selenium)
[Selenium][1] es un driver que automatiza interacciones con el explorador

Lo instalaremos y ejecutaremos como un paquete de nodejs, de esta manera
```bash
$ sudo npm install -g webdriver-manager
$ sudo webdriber-manager update
$ sudo webdriber-manager start
```



## Protractor
[Protractor][2] es un sistemas para ejecutar test e2e de aplicaciones angularjs, es decir, abre un explorador, (o no), y hace cliks, rellena campos y lo que haria el usuario de manera automatica. Como wrapper de selenium para angularjs, diremos que tambien se puede usar para aplicaciones no-angularjs

Lo instalamos en el sistema:
```bash
$ sudo npm install -g protractor
```
Y despues creamos un fichero de configuracion, como no tenemos angular hay que configurarlo con un par de cosillas

+ Diremos donde estan nuestros ficheros con tests de Jasmine en la variable specs
+ Y despues le diremos nuestros delays en la aplicacion, y que se olvide de la sincronizacion que hace con una app angular

```js
exports.config = {
  seleniumAddress: 'http://localhost:4444/wd/hub',
  specs: ['spec.js'],

  onPrepare: function() {
    // implicit and page load timeouts
    browser.manage().timeouts().pageLoadTimeout(20000);
    browser.manage().timeouts().implicitlyWait(10000);

    // for non-angular page
    browser.ignoreSynchronization = true;

    // Maximized chrome window
    browser.driver.manage().window().maximize();
  }
}
```


## Un test sencillo
Ahora crearemos un test sencillo, sacado el tutorial de protractor (muy util), en nuestro fichero specs.js:

```js
describe('angularjs homepage', function() {
  it('should have a title', function() {
    browser.get('http://juliemr.github.io/protractor-demo/');

    expect(browser.getTitle()).toEqual('Super Calculator');
  });
});
```

Y ejecutamos protractor:

```bash
$ protractor conf.js
```

## Chrome y PhantomJS
Hasta ahora estamos viendo nuestra ventana de chrome pasando los tests, pero si quisieramos pasarlos en un servidor de integracion continua, deberiamos usar un explorador headless, ya que es posible que este servidor no tenga servidor grafico para GUIs.

Para eso usaremos phantomjs, como en los anteriores paquetes:
```bash
$ sudo npm install -g phantomjs
```

Cambiaremos nuestro conf.js para que use phantomjs y ya lo tendremos headless.


[1]: http://docs.seleniumhq.org/projects/webdriver/
[2]: https://www.npmjs.org/package/protractor
