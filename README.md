# LOOK GATEWAY

Gateway IoT untuk menerima data sensor via MQTT, menyimpan ke database, dan menyediakan API untuk manajemen device.

## 🚀 Cara Menjalankan Gateway

1.  Pastikan virtual environment aktif:
    ```bash
    .\env\Scripts\Activate.ps1
    ```
2.  Jalankan server utama:
    ```bash
    py main.py
    ```
    *Tunggu sampai muncul pesan "Connected to MQTT Broker!".*



## 🔌 Informasi API (Untuk Integrasi)

Berikan informasi ini kepada developer Web App yang ingin terhubung ke Gateway.

*   **Base URL**: `http://[IP_GATEWAY]:5001`
*   **Token API**: `LOOK-SECURE-TOKEN-2024` (Wajib di Header)

### Endpoint: Tambah Device
*   **URL**: `/api/add_device`
*   **Method**: `POST`
*   **Headers**:
    *   `Content-Type`: `application/json`
    *   `X-API-TOKEN`: `LOOK-SECURE-TOKEN-2024`
*   **Body**:
    ```json
    {
      "device_name": "Sensor Kolam",
      "type_device": "temperature",
      "status": 1
    }
    ```
*   **Response Sukses**:
    ```json
    {
      "code": 200,
      "message": "Device berhasil ditambahkan",
      "device_id": "ID_001"
    }
    ```
