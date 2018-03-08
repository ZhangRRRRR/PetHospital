### ENVIROMENT FOR DEV CONFIGURATION ###

* install node.js v9.7.1

  * (optional) you can download node.js version 9.7.1 by using nvm * (node version manager) if you want to keep multiple versions of nodejs on your computer.
  * (warning) nvm does not have a windows version, nvm-windows is completely a seperate version, you need to uninstall any existing versions of node.js before installing NVM for Windows. Also delete any existing nodejs installation directories (e.g., "C:\Program Files\nodejs") that might remain.

  * (optional) download nvm:
    https://github.com/coreybutler/nvm-windows/releases
  * (optional) use nvm to download nodejs and use current version and use it:
  ```
    nvm install 9.7.1
    nvm use 9.7.1
  ```
    instructions here : https://github.com/coreybutler/nvm-windows
  
  * (not using nvm) directly download nodejs from official website:
    https://nodejs.org/en/download/releases/
    select 9.7.1 and download .msi executable and install

  * type "node -v" to check your installation
  ```
    node -v
  ```

  * npm 5.6.0 is included automatically by nodejs 9.7.1, type "npm -version" to check your npm installation
  ```
    npm -version
  ```

* (optional) install cnpm to accelerate your installation of npm packages

  * install cnpm
  ```
    npm install cnpm -g
  ```

  * check your cnpm installation
  ```
    cnpm -v
  ```

* install vue-cli package

  ```
    npm install -g vue-cli
  ```

* run your project

  * cd to a place
  ```
    cd d:/dev
  ```

  * 创建一个基于 webpack 模板的新项目 (use webpack template)
  ```
    vue init webpack [project_name]

    and follow the steps
  ```

  * cd to your project dir
  ```
    cd [project_name]
  ```

  * install all package dependencies
  ```
    cnpm install
  ```