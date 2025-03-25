# uuidtointarray
Convert UUID (standard format) into integer array format. Primary use in Minecraft NBT data.

This script:
1. Converts the UUID string into a UUID object.
2. Extracts the **Most Significant Bits (MSB)** and **Least Significant Bits (LSB)**.
3. Converts them to **signed 64-bit integers**.
4. Splits them into **four 32-bit signed integers**.
5. Returns the formatted integer array.

Example output for UUID `fee27a98-02b6-46d5-9f79-0614f58824b6`:

    `UUID:[I;-18711912,45500117,-1619458540,-175627082]`