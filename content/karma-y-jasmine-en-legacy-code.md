Title: Protractor en legacy code
Date: 2014-10-30 10:20
Category: js
Tags:tests,jasmine,node,js,javascript


#### Introduccion
Digamos que entras en un proyecto donde existe una aplicacion con varios años en produccion, que usa como unicas librerias require y jQuery, todo lo demas esta hecho a mano, ademas como puedes suponer, no tiene ni un solo test.

Nos proponemos hacer tests sobre el codigo existente y asi implantarlos para futuras features.

#### WebdriverJs (Selenium)
##### TODO

#### Protractor
Protractor es un sistemas para ejecutar test e2e de aplicaciones angularjs, es decir, abre un explorador, (o no), y hace cliks, rellena campos y lo que haria el usuario de manera automatica.

Lo instalamos en el sistema:
```
sudo npm install -g protractor
```
Y despues creamos un fichero de configuracion, como no tenemos angular hay que configurarlo con un par de cosillas

+ Diremos donde estan nuestros ficheros con tests de Jasmine en la variable specs
+ Y despues le diremos nuestros delays en la aplicacion, y que se olvide de la sincronizacion que hace con una app angular
```
// conf.js
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


