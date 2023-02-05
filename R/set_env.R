#' Settings
#'
#' Creates a virtual environment with needed libs
#' for the functions of soccerdatas package.
#'
#' @return set the configuration needed for the libs used on package.
#' @export set_env
#' @importFrom "reticulate" "virtualenv_create"
#' @examples set_env()


# set_env = function () {

#   reticulate::virtualenv_create(envname = '~/.env',
#                                 python = NULL,
#                                 version = '3.8.7',
#                                 packages=c('numpy','pandas','selenium'),
#                                 pip_options = character('python3 -m pip install --upgrade pip'))
#   os = Sys.info()[1]

#   if (os == "Windows") {
#     Sys.setenv(RETICULATE_PYTHON='~/.env/Scripts')
#     reticulate::virtualenv_install(envname = "~/.env", packages = "webdriver-manager",
#                                    ignore_installed = T)
#   } else {
#     Sys.setenv(RETICULATE_PYTHON='~/.env/bin')
#     reticulate::virtualenv_install(envname = "~/.env", packages = "webdriver-manager",
#                                    ignore_installed = T)
#   }

# }

########################################################################################################

set_env = function () {

  reticulate::virtualenv_create(envname = paste0(path.package('soccerdatas'),'/.env'),
                                python = NULL,
                                #version = '3.8.7',
                                packages=c('numpy','pandas','selenium'),
                                pip_options = character('python3 -m pip install --upgrade pip'))

  os = Sys.info()[1]

  if (os == "Windows") {
    Sys.setenv(RETICULATE_PYTHON=paste0(path.package('soccerdatas'),'/.env/Scripts'))
    reticulate::virtualenv_install(envname = paste0(path.package('soccerdatas'),'/.env'), packages = "webdriver-manager",
                                   ignore_installed = T)
  } else {
    Sys.setenv(RETICULATE_PYTHON=paste0(path.package('soccerdatas'),'/.env/bin'))
    reticulate::virtualenv_install(envname = paste0(path.package('soccerdatas'),'/.env'), packages = "webdriver-manager",
                                   ignore_installed = T)
  }

}