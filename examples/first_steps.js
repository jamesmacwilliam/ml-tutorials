import tf from '@tensorflow/tfjs'
import { Series, DataFrame } from 'pandas-js'
import request from 'request'
import fs from 'fs'
import getStream from 'get-stream'
import parse from 'csv-parse'

let housing_file = "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv"
let parser = parse({ delimiter: ',', columns: true })

let housingTests = async () => {
  let parsed = await getStream.array(request(housing_file).pipe(parser))
  let df = new DataFrame(parsed)
  //console.log(df.get('latitude'))
  //console.log(df.columns)
  let old = new DataFrame({ old: df.get('housing_median_age').map((val, idx) => val > 20) })
  console.log(old)
}

housingTests()
