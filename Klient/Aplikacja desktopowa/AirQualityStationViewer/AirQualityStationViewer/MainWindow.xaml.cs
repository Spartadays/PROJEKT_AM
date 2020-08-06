using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Net;
using System.IO;
using Newtonsoft.Json;

namespace AirQualityStationViewer
{
    /// <summary>
    /// Logika interakcji dla klasy MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private string rpi_ip = "192.168.1.68";
        public MainWindow()
        {
            InitializeComponent();
            textbox_ip.Text = rpi_ip;
        }

        private void Button_show_epaper_Click(object sender, RoutedEventArgs e)
        {
            string sURL = "http://" + rpi_ip + "/epaper_show.php";
            WebRequest wrGETURL;
            wrGETURL = WebRequest.Create(sURL);
            try
            {
                wrGETURL.GetResponse();
            }
            catch { }
        }

        private void Clear_epaper_Click(object sender, RoutedEventArgs e)
        {
            string sURL = "http://" + rpi_ip + "/clear.php";
            WebRequest wrGETURL;
            wrGETURL = WebRequest.Create(sURL);
            try
            {
                wrGETURL.GetResponse();
            }
            catch { }
        }

        private void Button_get_distance_Click(object sender, RoutedEventArgs e)
        {
            string sURL = "http://" + rpi_ip + "/distance.php";
            WebRequest wrGETURL;
            wrGETURL = WebRequest.Create(sURL);
            Stream objStream;
            try
            {
                objStream = wrGETURL.GetResponse().GetResponseStream();

                StreamReader objReader = new StreamReader(objStream);

                string sLine = "";
                int i = 0;

                while (sLine != null)
                {
                    i++;
                    sLine = objReader.ReadLine();
                    if (sLine != null)
                    {
                        Console.WriteLine("{0}:{1}", i, sLine);
                        distance.Text = sLine + " cm";
                    }

                }
            }
            catch { }
            //Console.ReadLine();
        }

        private void Button_send_epaper_Click(object sender, RoutedEventArgs e)
        {
            string sURL = "http://" + rpi_ip + "/send_text_epaper.php?text='" + textbox_epaper.Text + "'";
            WebRequest wrGETURL;
            wrGETURL = WebRequest.Create(sURL);
            try
            {
                wrGETURL.GetResponse();
            }
            catch { }
        }

        private void Button_show_airqualitystation_Click(object sender, RoutedEventArgs e)
        {
            string sURL = "https://api.thingspeak.com/channels/775759/feeds.json?results=1";
            var json = new WebClient().DownloadString(sURL);
            dynamic stuff = JsonConvert.DeserializeObject(json);
            l1.Content = stuff.channel.field1;
            l2.Content = stuff.channel.field2;
            l3.Content = stuff.channel.field3;
            l4.Content = stuff.channel.field4;
            l5.Content = stuff.channel.field5;
            l6.Content = stuff.channel.field6;
            l7.Content = stuff.channel.field7;
            l8.Content = stuff.channel.field8;
            l9.Content = stuff.channel.name;
            l1_C.Content = stuff.feeds[0].field1;
            l2_C.Content = stuff.feeds[0].field2;
            l3_C.Content = stuff.feeds[0].field3;
            l4_C.Content = stuff.feeds[0].field4;
            l5_C.Content = stuff.feeds[0].field5;
            l6_C.Content = stuff.feeds[0].field6;
            l7_C.Content = stuff.feeds[0].field7;
            l8_C.Content = stuff.feeds[0].field8;
            l9_C.Content = stuff.channel.id;
            Console.WriteLine(stuff);
        }

        private void Button_ip_Click(object sender, RoutedEventArgs e)
        {
            rpi_ip = textbox_ip.Text;
        }
    }
}
