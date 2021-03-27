#' Web scraping of serie b
#'
#' Open Firefox browser in GE website simulating a user
#' collecting the local of match, scoreboard and the team names
#'
#' @return two tables with the matches played and future matches
#' @export serie_b
#'
#' @examples
#' serie_b()
serie_b = function() {
  if ('reticulate' %in% rownames(installed.packages())) {
    reticulate::py_run_file('Python/scrapingGE_B.py')
  } else {
    install.package('reticulate')
    reticulate::py_run_file('Python/scrapingGE_B.py')
  }
}
