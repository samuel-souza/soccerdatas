#' Web scraping of serie a
#'
#' Open Firefox browser in GE website simulating a user
#' collecting the local of match, scoreboard and the team names
#' @return two tables with the matches played and future matches
#' @export serie_a
#'
#' @importFrom "reticulate" "py_run_file"
#' @importFrom "utils" "install.packages" "installed.packages" "read.csv"
#' @examples
#' serie_a()


serie_a = function() {

  if ('reticulate' %in% rownames(utils::installed.packages())){
  reticulate::py_run_file('./inst/python/ScrapingGE_A.py')
  } else {
    utils::install.packages('reticulate')
  reticulate::py_run_file('./inst/python/ScrapingGE_A.py')
  }

  .GlobalEnv$database = utils::read.csv('dtbase.csv')
  .GlobalEnv$future_matches = utils::read.csv('fmatches.csv')
  file.remove(c('dtbase.csv','fmatches.csv'))
}

