#' Web scraping of PB championship
#'
#' Open Firefox browser in GE website simulating a user
#' collecting the local of match, scoreboard and the team names
#'
#' @return two tables with the matches played and future matches
#' @export PB
#'
#' @importFrom "utils" "read.csv"
#' @importFrom "reticulate" "py_run_file"
#'
#' @examples PB()

PB = function() {

  Sys.getenv("RETICULATE_PYTHON")
  reticulate::use_virtualenv(virtualenv='~/.env',required=T)
  setwd(paste0(as.character(path.package('soccerdatas')),'/python'))
  reticulate::py_run_file(paste0(path.package('soccerdatas'),'/python/PB.py'))

  .GlobalEnv$database = utils::read.csv(paste0(path.package('soccerdatas'),'/python/dtbase.csv'))
  .GlobalEnv$future_matches = utils::read.csv(paste0(path.package('soccerdatas'),'/python/fmatches.csv'))
  file.remove(c('dtbase.csv','fmatches.csv'))

}
