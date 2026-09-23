import { useEffect, useMemo, useState } from 'react'

const PACKAGE_OPTIONS = [
  { code: 'STD', label: 'แพ็กเกจมาตรฐาน' },
  { code: 'PREMIUM', label: 'แพ็กเกจพรีเมียม' },
]

export default function SlotPicker({ client, initialPackageCode = 'STD' }) {
  const [packageCode, setPackageCode] = useState(initialPackageCode)
  const [slots, setSlots] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const dateFrom = useMemo(() => {
    const today = new Date()
    today.setHours(0, 0, 0, 0)
    return today.toISOString().slice(0, 10)
  }, [])

  useEffect(() => {
    const loadSlots = async () => {
      setLoading(true)
      setError('')

      try {
        const data = client
          ? await client.getSlots({ dateFrom, packageCode })
          : []
        setSlots(Array.isArray(data) ? data : [])
      } catch {
        setError('ไม่สามารถโหลดช่วงเวลาว่างได้')
        setSlots([])
      } finally {
        setLoading(false)
      }
    }

    loadSlots()
  }, [client, dateFrom, packageCode])

  return (
    <section className="mx-auto max-w-2xl rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h2 className="text-xl font-bold text-slate-800">เลือกแพ็กเกจ</h2>

      <div className="mt-4 flex gap-3">
        {PACKAGE_OPTIONS.map((option) => (
          <button
            key={option.code}
            type="button"
            onClick={() => setPackageCode(option.code)}
            className={[
              'rounded-lg border px-4 py-2 text-sm font-medium transition',
              packageCode === option.code
                ? 'border-teal-600 bg-teal-600 text-white'
                : 'border-slate-300 bg-white text-slate-700 hover:bg-slate-50',
            ].join(' ')}
          >
            {option.label}
          </button>
        ))}
      </div>

      <div className="mt-6">
        <h3 className="text-lg font-semibold text-slate-800">ช่วงเวลาว่าง</h3>

        {loading && <p className="mt-3 text-slate-600">กำลังโหลดช่วงเวลา...</p>}
        {error && <p className="mt-3 text-red-600">{error}</p>}

        {!loading && !error && slots.length === 0 && (
          <p className="mt-3 text-slate-600">ไม่มีช่วงเวลาว่างสำหรับแพ็กเกจนี้</p>
        )}

        <ul className="mt-4 space-y-3">
          {slots.map((slot) => (
            <li
              key={slot.id}
              className="flex items-center justify-between rounded-lg border border-slate-200 p-3"
            >
              <div>
                <p className="font-medium text-slate-800">{slot.start_time}</p>
                <p className="text-sm text-slate-500">{slot.slot_date}</p>
              </div>
              <span className="text-sm text-slate-700">มีที่นั่งคงเหลือ: {slot.remaining}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}
