if (typeof kotlin === 'undefined') {
  throw new Error("Error loading module 'Inventory-PurpleCurves'. Its dependency 'kotlin' was not found. Please, check whether 'kotlin' is loaded prior to 'Inventory-PurpleCurves'.");
}this['Inventory-PurpleCurves'] = function (_, Kotlin) {
  'use strict';
  var println = Kotlin.kotlin.io.println_s8jyv4$;
  function main(args) {
    println('ola');
  }
  _.main_kand9s$ = main;
  main([]);
  Kotlin.defineModule('Inventory-PurpleCurves', _);
  return _;
}(typeof this['Inventory-PurpleCurves'] === 'undefined' ? {} : this['Inventory-PurpleCurves'], kotlin);
