# A general collection of useful demo assets

`FugueDemo.lw` is the basic standard "Hello World!" Fugue demo composition.

`App.lw` uses `Services/CommonBackend.lw` as a service catalog for a basic workload that mirrors `FugueDemo.lw`. Meant to show how to create your own service catalog abstractions. 

`PriceExample.lw` shows how to use Node Stream validations with a per hour budget. (Note: Use the price validations repo https://github.com/LuminalHQ/price-validations directly for a more thorough demo of this. This is just a handy local copy, and incomplete for how that project works).

`ImportTemplate.lw` can be run to spin up some useful resources tagged as "MobileApp" for subsequent use with Transcriber. Note that the DDB table must be manually tagged to complete the process (Fugue DDB does not yet support DDB tagging). Also remember to fun `fugue release` on this.

Make and Jenkins can be used for CI/CD demos. Talk to Sabo or Sage for more detail on that.

