import SlotPicker from './pages/SlotPicker.jsx'

export default function App() {
  const mockClient = {
    async getSlots({ dateFrom, packageCode }) {
      const slots = {
        STD: [
          { id: 1, slot_date: dateFrom, start_time: '09:00', remaining: 2, package_code: 'STD' },
          { id: 2, slot_date: dateFrom, start_time: '11:00', remaining: 3, package_code: 'STD' },
        ],
        PREMIUM: [
          { id: 3, slot_date: dateFrom, start_time: '10:00', remaining: 1, package_code: 'PREMIUM' },
        ],
      }

      return slots[packageCode] ?? []
    },
  }

  return (
    <main className="mx-auto max-w-2xl p-6">
      <h1 className="text-2xl font-bold text-teal-800">ระบบจองคิวตรวจสุขภาพ</h1>
      <div className="mt-6">
        <SlotPicker client={mockClient} />
      </div>
    </main>
  )
}
