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

