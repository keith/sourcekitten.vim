" autocmd InsertLeave * update | call swift#Go()
autocmd TextChanged,TextChangedI * call swift#Go()
