using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Accord.Video.FFMPEG;
using AForge.Video;
using AForge.Video.DirectShow;
using VisioForge.Libs.AForge.Imaging.Filters;

namespace GUI_GP
{
    public partial class realTimeForm : Form
    {
        Form GUI;

        private FilterInfoCollection videoDevices;
        private VideoCaptureDevice videoSource;
        private VideoFileWriter _writer;
        private DateTime? _firstFrameTime;
        private int i = 0;
        private DateTime _lastSavedFrameTime = DateTime.MinValue;
        private int _frameCount = 0;
        public realTimeForm(Form mainGUI)
        {
            InitializeComponent();
            photoBox.Image = Properties.Resources._179_1796406_thinking_man_download_transparent_png_image_man_thinking;
            GUI = mainGUI;
        }

        private void realTimeForm_FormClosing(object sender, FormClosingEventArgs e)
        {


            if (videoSource != null && videoSource.IsRunning)
            {
                videoSource.SignalToStop();
                videoSource.WaitForStop();

            }
            Application.ExitThread();
            Application.Exit();

        }
        private void videoSource_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            // Update the picture box with the new frame
            pic.Image = (Bitmap)eventArgs.Frame.Clone();
            Bitmap image = (Bitmap)eventArgs.Frame.Clone();
            _writer.WriteVideoFrame(image);
            if ((DateTime.Now - _lastSavedFrameTime).TotalSeconds >= 2)
            {
                image.Save("../../../../frame_realtime/" + i.ToString() + ".jpg");
                i++;
                _lastSavedFrameTime = DateTime.Now;
                _frameCount++;
               
            }
            readOutputs();

            //_writer.WriteVideoFrame(image);



        }
        private void readOutputs()
        {
            
            string facePath = "../../../../files/face.txt";

            string[] faceFromFile = File.ReadAllLines(facePath);

            string weaponPath = "../../../../files/guns.txt";
            string[] weaponFromFile = File.ReadAllLines(weaponPath);

            string firePath = "../../../../files/detect_fire.txt";
            string[] fireFromFile = File.ReadAllLines(firePath);

            if (faceFromFile.Length != 0)
            {
                string x = "../../../";
                string[] person = faceFromFile[0].Split(',');
                photoBox.Image = Image.FromFile(x+person[0]);
                if (nameRealTxt.InvokeRequired)
                {
                    // Use Invoke to access the control from the UI thread
                    nameRealTxt.Invoke((MethodInvoker)delegate
                    {
                        nameRealTxt.Text = person[1];

                    });
                }
            }
            if (weaponFromFile.Length != 0)
            {
                if (weaponRealTxt.InvokeRequired)
                {
                    // Use Invoke to access the control from the UI thread
                    weaponRealTxt.Invoke((MethodInvoker)delegate
                    {
                        weaponRealTxt.Text = weaponFromFile[0];

                    });
                }
            }
            if (fireFromFile.Length != 0)
            {
                if (fireRealTxt.InvokeRequired)
                {
                    // Use Invoke to access the control from the UI thread
                    fireRealTxt.Invoke((MethodInvoker)delegate
                    {
                        fireRealTxt.Text = fireFromFile[0];

                    });
                }

            }

        }

        private void realTimeForm_Load(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter("../../../../files/location of videos.txt"))
            {
                writer.WriteLine("0");
                writer.Write("../frame_realtime");

            }
            _writer = new VideoFileWriter();
            _writer.Open("../../../../realtime/test.avi", 640, 360);
            // Get available video devices
            videoDevices = new FilterInfoCollection(FilterCategory.VideoInputDevice);

            // Create the video capture device using the first available device
            videoSource = new VideoCaptureDevice(videoDevices[0].MonikerString);
            videoSource.NewFrame += new NewFrameEventHandler(videoSource_NewFrame);
            
            // Start capturing
            videoSource.Start();


        }

        private void pic_Click(object sender, EventArgs e)
        {

        }

        private void photoBox_Click(object sender, EventArgs e)
        {

        }
    }
}
