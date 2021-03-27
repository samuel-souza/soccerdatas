#' Web scraping of serie a
#'
#' Open Firefox browser in GE website simulating a user
#' collecting the local of match, scoreboard and the team names
#' @return two tables with the matches played and future matches
#' @export serie_a
#'
#' @examples
#' serie_a()


serie_a = function() {
  if ('reticulate' %in% rownames(installed.packages())){
  reticulate::py_run_file('Python/ScrapingGE_A.py')
  } else {
    install.packages('reticulate')
  reticulate::py_run_file('Python/ScrapingGE_A.py')
  }

  database <<- utils::read.csv('dtbase.csv')
  future_matches <<- utils::read.csv('fmatches.csv')
  file.remove(c('dtbase.csv','fmatches.csv'))
}

