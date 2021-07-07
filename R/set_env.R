#' Settings
#'
#' Creates a virtual environment with needed libs
#' for the functions of soccerdatas package.
#'
#' @return set the configuration needed for the libs used on package.
#' @export set_env
#' @importFrom "reticulate" "virtualenv_create"
#' @examples set_env()


set_env = function () {

  reticulate::virtualenv_create(envname = '~/.env',
                                python = NULL,
                                version = '3.8.7',
                                packages = c('numpy','pandas','selenium'),
                                pip_options = character('pip install webdriver_manager')
                                )
  Sys.setenv(RETICULATE_PYTHON='~/.env/Scripts')

}
