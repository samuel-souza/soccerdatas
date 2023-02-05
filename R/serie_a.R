#' Web scraping of serie a
#'
#' Open Firefox browser in GE website simulating a user
#' collecting the local of match, scoreboard and the team names
#'
#' @return two tables with the matches played and future matches
#' @export serie_a
#'
#' @importFrom "utils" "read.csv"
#' @importFrom "reticulate" "py_run_file"
#'
#' @examples serie_a()


serie_a = function() {

  Sys.getenv("RETICULATE_PYTHON")
  dir = getwd()
  setwd(as.character(path.package('soccerdatas')))
  reticulate::py_run_file(paste0(path.package('soccerdatas'),'/python/scrapingGE_A.py'))

  .GlobalEnv$database = utils::read.csv('dtbase.csv')
  .GlobalEnv$future_matches = utils::read.csv('fmatches.csv')
  file.remove(c('dtbase.csv','fmatches.csv'))
  setwd(dir)
}
