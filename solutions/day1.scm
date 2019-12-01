(use extras)

(define (get-fuel-from-mass mass)
  (max 0 (- (floor (/ mass 3.0)) 2)))

(define (get-extra-fuel-from-mass mass)
  (letrec ((loop (lambda (sum additional)
                   (if (<= additional 0)
                     sum
                     (loop (+ sum (get-fuel-from-mass additional)) (get-fuel-from-mass additional))))))
           (loop 0 mass)))

;; part 1
(with-input-from-file "input"
                      (lambda ()
                        (let loop ((sum 0) (line (read-line)))
                          (if (eof-object? line)
                              (begin (display sum) (newline))
                              (loop (+ sum (get-fuel-from-mass (string->number line))) (read-line))))))

;; part 2
(with-input-from-file "input"
                      (lambda ()
                        (let loop ((sum 0) (line (read-line)))
                          (if (eof-object? line)
                              (begin (display sum) (newline))
                              (loop (+ sum (get-extra-fuel-from-mass (string->number line))) (read-line))))))
