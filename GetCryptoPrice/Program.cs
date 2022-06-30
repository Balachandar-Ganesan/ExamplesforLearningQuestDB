using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Net;
using System.Diagnostics;
using QuestDB;

namespace Tester
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Stopwatch timer = new Stopwatch();
            timer.Start();
            /* change the value 10 to interval you want 60 for a minute,3600 for an hour*/
            while (timer.Elapsed.TotalSeconds < 10)
            {
                await TestCoinsAsync();
                
            }
            timer.Stop();
            Console.WriteLine("Price retrieved");
        }


        static async Task TestCoinsAsync()
        {
            string json;

            using (var web = new System.Net.WebClient())
            {
                var url = @"https://api.coindesk.com/v1/bpi/currentprice.json";
                json = web.DownloadString(url);
            }

            dynamic obj = Newtonsoft.Json.JsonConvert.DeserializeObject(json);
            var currentPrice = Convert.ToDecimal(obj.bpi.USD.rate.Value);
            float BitCoinPrice = (float)currentPrice;    

            using var ls = await LineTcpSender.ConnectAsync("localhost", 9009, tlsMode: TlsMode.Disable);
            ls.Table("BitCoinPrice")
                .Symbol("name", "BTC-USD")
                .Column("value", BitCoinPrice)
                .AtNow();
            await ls.SendAsync();
            /* change the vaue below to increase the delay */
            Thread.Sleep(0);
        }

    }
}




