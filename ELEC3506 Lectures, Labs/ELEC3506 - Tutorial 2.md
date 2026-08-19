---
Sheet Link: "[Canvas](https://canvas.sydney.edu.au/courses/74305/files/50449352?module_item_id=3132104)"
---
---
### 1. Distinguish between a signal element and a data element.
**Data elements** are the pieces of information you send, like bits (0s and 1s)
**Signal elements** are the physical methods of sending the signals, eg:
- Voltage
- Pulses
- Light Flashes
- Radio Waves

### 2. Distinguish between data rate and signal rate
**Data rate (Bit rate)**: is the rate at which digital information/(data elements)/data bits are being transfered per second 
- Higher bit rate = More Data being sent through per second
**Signal rate (Baud rate)**: is the rate at which a signal changes (signal elements) per second, allowing it to carry that information
- Lower baud rate = Faster/More channel switches per second = More information able to be sent per second
$$
\begin{aligned}
&S \times r = N \\
Where:&\\
- &Signal\>Rate\> (Baud)\\
- &N = Data\>rate\>(bps)\\
- &Number\>of\>Data\>bits\>per\>Signal\>element
\end{aligned}
$$

### 3. Define the characteristics of a self-synchronizing signal
A self synchronyzing signal embeds a timing/clock into the data stream being sent, so a separate clock line isnt needed.
- Guaranteed to have constant periodic signals at each time interval
- **No clock slippage:** When extended constant signals are being sent (eg 50 1s), the receiver wont lose track of count of the flatline
- **No clock skew:** Because there is only one channel being sent (No separate clock channel needed), there is no risk of clock skew, which is where the clock channel arrives faster than the signal channel, which would otherwise cause issues in signals
- **Performance trade off:** Because more bandwidth and more signal flips are needed to hold the embedded clock, there is a trade off for maximum data efficiency for more reliable timing

### 4. What are the differences between parallel and serial transmission
**Serial transmissions:** Are transmissions that send 1 bit at a time in sequence over 1 channel
- More reliable as bits are transmitted in order
- Minimal risk of interference
- Single thin cable
**Parallel transmissions:** Sends multiple data streams at once across multiple channels with the same clock tick
- Less reliable as bits can arrive out of order
- Higher risk of interference as cluster of cables can interfere with each other
- Useful for short range componenets
	- Microchip, RAM, Hard drive ribbon cable

### 5. Discuss the steps of PCM
**PCM:** Pulse code modulation converts ==Analog== signal into ==Digital== bitstreams. 
1. **Bandlimiting**: analogue signal passes through filter to remove any frequencies that are higher than the desired frequency
2. **[[Sampling]]** The continous analogue time is measured at uniform regular time intervals, resulting in a series of pulses measuring the analogue heights > Pulse Amplitude 
3. **Quantization**: The amplitudes from the sample are rounded to the nearest predetermined discrete level
	- **Quantization Error:** The unavoidable tiny difference between the rounded discrete level and the exact analogue amplitude
	- **Liner vs Non-Linear Levels:** Step sizes between levels can either be uniform (linear) or non-linear to allow more levels for quieter signals and less for louder
4. **Encoding**: Each quantized level is converted into an *n-bit* binary code:
$$
L=2^n\ \ OR\ \ n=log_2 L
$$
	- **Output:** a digital bitstream of 1s and 0s ready for transmission with a bit rate of:
	$$R_b = n\,\cdot\,f_8 $$
### 6. Different techniques of Serial Transmission

|                   | **Asynchronous** | **Synchronous** | **Isochronous** |
| :---------------: | :--------------: | :-------------: | :-------------: |
|    *Mechanism*    |                  |                 |                 |
| *Synchronisation* |                  |                 |                 |
|     *Timing*      |                  |                 |                 |
|   *Efficiency*    |                  |                 |                 |
