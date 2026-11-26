import Foundation
import Vision
import CoreGraphics
import ImageIO

let dir = "/Users/konul/.gemini/antigravity/worktrees/esas2 copy 3/premium_university_interface/scratch_camscanner"

for i in 1...22 {
    let path = "\(dir)/page_\(String(format: "%02d", i)).jpg"
    guard let imgUrl = CFURLCreateWithFileSystemPath(kCFAllocatorDefault, path as CFString, .cfurlposixPathStyle, false),
          let src = CGImageSourceCreateWithURL(imgUrl, nil),
          let cgImg = CGImageSourceCreateImageAtIndex(src, 0, nil) else {
        continue
    }
    
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false
    
    let handler = VNImageRequestHandler(cgImage: cgImg, options: [:])
    try? handler.perform([request])
    
    let results = request.results ?? []
    print("=== PAGE \(i) ===")
    for obs in results {
        let text = obs.topCandidates(1).first?.string ?? ""
        print(text)
    }
    print("")
}
