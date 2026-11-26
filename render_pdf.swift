import Foundation
import PDFKit
import CoreGraphics

let pdfPath = "/Users/konul/Documents/esas2 copy 3/CamScanner 24.11.26 09.38.pdf"
let outDir = "/Users/konul/.gemini/antigravity/worktrees/esas2 copy 3/premium_university_interface/scratch_camscanner"

try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)

guard let doc = PDFDocument(url: URL(fileURLWithPath: pdfPath)) else {
    print("Failed to open PDF")
    exit(1)
}

print("Total pages:", doc.pageCount)

for i in 0..<doc.pageCount {
    guard let page = doc.page(at: i) else { continue }
    let pageRect = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2.0 // high resolution
    let width = Int(pageRect.width * scale)
    let height = Int(pageRect.height * scale)
    
    let colorSpace = CGColorSpaceCreateDeviceRGB()
    guard let ctx = CGContext(data: nil, width: width, height: height, bitsPerComponent: 8, bytesPerRow: 0, space: colorSpace, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { continue }
    
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: width, height: height))
    
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    
    guard let img = ctx.makeImage() else { continue }
    let destUrl = URL(fileURLWithPath: "\(outDir)/page_\(String(format: "%02d", i + 1)).jpg")
    guard let destination = CGImageDestinationCreateWithURL(destUrl as CFURL, "public.jpeg" as CFString, 1, nil) else { continue }
    let properties: [CFString: Any] = [kCGImageDestinationLossyCompressionQuality: 0.85]
    CGImageDestinationAddImage(destination, img, properties as CFDictionary)
    CGImageDestinationFinalize(destination)
    print("Rendered page \(i + 1)")
}
