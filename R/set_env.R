#' Settings
#'
#' Creates a virtual environment with needly libs
#' for the functions of soccerdatas package.
#'
#' @return set the configuration needed for the libs used on package.
#' @export set_ve
#' @importFrom "reticulate" "virtualenv_create"
#' @examples set_ve()

set_ve = function () {


  reticulate::virtualenv_create(envname = '~/.env',
                                python = NULL,
                                packages = c('numpy','pandas','selenium'))

  Sys.setenv(RETICULATE_PYTHON='~/.env/Scripts')

}
