#' Database general of serie a 2020
#'
#' @return table with all the matches played in 2020
#' @export data.general_a
#'
#' @examples
#' data.general_a()
data.general_a = function() {
  dtg_a <<- utils::read.csv('Database/2020a.csv')
}
