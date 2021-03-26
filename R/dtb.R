dtb.2020_a = function(csvFile,...) {

  dtb_2020 <<- utils::read.csv(csvFile,...)
  return(dtb_2020[,2:5])

}
