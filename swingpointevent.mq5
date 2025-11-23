//+------------------------------------------------------------------+
//|               SwingDetector_5by5.mq5                             |
//|  Detects Swing Highs & Lows using 5-bar left/right comparison    |
//|  Pure MQL5 EA, NO MT4-style functions                            |
//+------------------------------------------------------------------+
#property strict

input int Lookback = 200;        // candles to scan
input int LeftBars = 5;          // number of bars to the left
input int RightBars = 5;         // number of bars to the right

//--- Arrays to store swing points
double SwingHighBuffer[];
double SwingLowBuffer[];

//------------------------------------------------------------------+
int OnInit()
{
   ArraySetAsSeries(SwingHighBuffer, true);
   ArraySetAsSeries(SwingLowBuffer, true);

   Print("Swing Detector Initialized.");
   return(INIT_SUCCEEDED);
}
//------------------------------------------------------------------+
void OnTick()
{
   DetectSwings();
}
//------------------------------------------------------------------+
void DetectSwings()
{
   int bars = MathMin(Bars - RightBars - 1, Lookback);
   if(bars <= LeftBars + RightBars) return;

   for(int i = LeftBars; i <= bars; i++)
   {
      double high = High[i];
      double low  = Low[i];

      bool isSwingHigh = true;
      bool isSwingLow  = true;

      //--- compare left and right
      for(int j = 1; j <= LeftBars; j++)
      {
         if(High[i] <= High[i+j]) isSwingHigh = false;
         if(Low[i]  >= Low[i+j]) isSwingLow  = false;
      }

      for(int j = 1; j <= RightBars; j++)
      {
         if(High[i] <= High[i-j]) isSwingHigh = false;
         if(Low[i]  >= Low[i-j]) isSwingLow  = false;
      }

      //--- store and draw objects
      if(isSwingHigh)
      {
         SwingHighBuffer[i] = high;
         DrawSwingPoint(i, high, "SH_");
      }
      if(isSwingLow)
      {
         SwingLowBuffer[i] = low;
         DrawSwingPoint(i, low, "SL_");
      }
   }
}
//------------------------------------------------------------------+
void DrawSwingPoint(int index, double price, string prefix)
{
   string name = prefix + IntegerToString(index);

   if(ObjectFind(0, name) != -1) return;

   ObjectCreate(0, name, OBJ_ARROW, 0, Time[index], price);
   ObjectSetInteger(0, name, OBJPROP_COLOR, (prefix == "SH_" ? clrRed : clrBlue));
   ObjectSetInteger(0, name, OBJPROP_WIDTH, 2);
   ObjectSetInteger(0, name, OBJPROP_ARROWCODE, (prefix == "SH_" ? 233 : 234)); // Up/Down arrows
}
//------------------------------------------------------------------+
